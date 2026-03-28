import torch
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset

from src.Set_Processor import ImportData


def train_transformer_pipeline(X_data, y_data):
    print("\n" + "=" * 60)
    print("🚀 TRENOWANIE TRANSFORMERA (DistilBERT) PRZEZ HUGGING FACE")
    print("=" * 60)

    # 1. Przygotowanie danych (Pandas -> Lista)
    print("Konwersja danych do formatu Hugging Face...")
    X_train, X_test, y_train, y_test = train_test_split(
        X_data.tolist(),
        y_data.tolist(),
        test_size=0.3,
        random_state=42
    )

    # Hugging Face uwielbia własny format "Dataset" zamiast zwykłych list/tensorów
    train_dataset = Dataset.from_dict({'text': X_train, 'label': y_train})
    test_dataset = Dataset.from_dict({'text': X_test, 'label': y_test})

    # 2. Inicjalizacja Tokenizatora (Gotowy słownik od inżynierów z Hugging Face)
    model_name = "distilbert-base-uncased"
    print(f"\nPobieranie pre-trenowanego tokenizatora: {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Funkcja, która zamieni tekst na tensory
    def tokenize_function(examples):
        # max_length=128 ucina za długie linki (chroni Twój RAM i VRAM)
        return tokenizer(examples['text'], padding="max_length", truncation=True, max_length=128)

    print("Tokenizacja całego zbioru (to może chwilę potrwać)...")
    tokenized_train = train_dataset.map(tokenize_function, batched=True)
    tokenized_test = test_dataset.map(tokenize_function, batched=True)

    # 3. Pobranie Modelu
    print(f"\nPobieranie potężnego modelu językowego: {model_name}...")
    # num_labels=2, bo nasza klasyfikacja to tylko 0 (Bezpieczny) i 1 (Phishing)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

    # 4. Definicja metryk do pracy magisterskiej
    def compute_metrics(pred):
        labels = pred.label_ids
        preds = pred.predictions.argmax(-1)
        precision, recall, f1, _ = precision_recall_fscore_support(labels, preds, average='binary')
        acc = accuracy_score(labels, preds)
        return {
            'accuracy': acc,
            'f1': f1,
            'precision': precision,
            'recall': recall
        }

    # 5. Konfiguracja "Pipeline'u" (Trener z pełną automatyzacją)
    training_args = TrainingArguments(
        output_dir='./wyniki_transformer',
        learning_rate=2e-5,  # Bardzo mały krok uczenia (model jest już mądry, tylko go "dotrenowujemy")
        per_device_train_batch_size=64,  # Zmniejszone by nie zepsuć VRAM
        per_device_eval_batch_size=128,
        num_train_epochs=3,  # Transformery uczą się błyskawicznie, 3 epoki w zupełności wystarczą!
        weight_decay=0.01,
        eval_strategy="epoch",  # Ewaluacja po każdej epoce
        save_strategy="epoch",
        load_best_model_at_end=True,  # Na koniec pipeline sam wybierze najlepszą wersję
        fp16=True,  # 🔥 MAGIA GPU: 16-bitowa precyzja oszczędza połowę pamięci VRAM!
        logging_dir='./logs',
        logging_steps=100,
    )

    # 6. Uruchomienie profesjonalnego Trenera
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_train,
        eval_dataset=tokenized_test,
        compute_metrics=compute_metrics,
    )

    print("\n" + "🔥" * 20)
    print("ROZPOCZYNAMY TRANSFER LEARNING!")
    print("🔥" * 20)
    trainer.train()

    # 7. Wyniki i Raport
    print("\nOstateczna ewaluacja na zbiorze testowym:")
    results = trainer.evaluate()
    print(f"F1-Score:  {results['eval_f1']:.4f}")
    print(f"Precision: {results['eval_precision']:.4f}")
    print(f"Recall:    {results['eval_recall']:.4f}")

    print("\nGenerowanie Macierzy Pomyłek...")
    predictions = trainer.predict(tokenized_test)
    y_pred = predictions.predictions.argmax(-1)

    print("\nMACIERZ POMYŁEK (TRANSFORMER):")
    print(confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    X, y = ImportData().Get_Scalet_sets()
    train_transformer_pipeline(X, y)